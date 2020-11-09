# An example of setting up an event handling pipeline with coroutines
# and XML parsing.

# This code will filter xml elements from the given conditions i:e ("route","22")
# and process it as a dict

from starting_coroutine_using_decorator import start_coroutine

@start_coroutine
def buses_to_dicts(target):
    while True:
        event, value = (yield)
        print("buses_to_dicts event, value", event, value[0])
        # Look for the start of a <bus> element
        if event == 'start' and value[0] == 'bus':
            busdict = { }
            fragments = []
            # Capture text of inner elements in a dict
            while True:
                event, value = (yield)
                if event == 'start':   fragments = []
                elif event == 'text':  fragments.append(value)
                elif event == 'end':
                    if value != 'bus':
                        busdict[value] = "".join(fragments)
                    else:
                        target.send(busdict)
                        break

@start_coroutine
def filter_on_field(fieldname,value,target):
    while True:
        d = (yield)
        print("filter_on_field d",d)
        if d.get(fieldname) == value:
            target.send(d)

@start_coroutine
def bus_locations():
    while True:
        bus = (yield)
        print("%(route)s,%(id)s,\"%(direction)s\","\
              "%(latitude)s,%(longitude)s" % bus)

# Example
if __name__ == '__main__':
    import xml.sax
    from cosax_eventhandler import EventHandler

    xml.sax.parse("allroutes.xml",
              EventHandler(
                   buses_to_dicts(
                   filter_on_field("route","22",
                   filter_on_field("direction","North Bound",
                   bus_locations())))
              ))