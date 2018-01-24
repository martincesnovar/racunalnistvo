# =============================================================================
# Vrsta z dvema skladoma
# =====================================================================@010442=
# 1. podnaloga
# Izkaže se, da lahko vrsto implementiramo z uporabo dveh skladov. Kako točno,
# ugotovite sami s pomočjo priložene implementacije v Javi. Vaša naloga je,
# da kodo pretvorite v Python in implementirate razred `Vrsta`, ki naj ima
# naslednje metode:
# 
# * konstruktor `__init__(self)`;
# * `vstavi(self, vsebina)`, ki v vrsto vstavi element `vsebina`;
# * `prazna(self)`, ki vrne `True`, če je vrsta prazna;
# * `zacetek(self)`, ki vrne element na začetku vrste;
# * `odstrani(self)`, ki odstrani element na začetku vrste.
# 
# Primer:
# 
#     >>> v = Vrsta()
#     >>> v.vstavi(3)
#     >>> v.vstavi(4)
#     >>> v.prazna()
#     False
#     >>> v.zacetek()
#     3
#     >>> v.odstrani()
#     >>> v.zacetek()
#     4
#     >>> v.odstrani()
#     >>> v.prazna()
#     True
# =============================================================================
from sklad import Sklad

class Vrsta:
    def __init__(self):
        self.sklad1 = Sklad()
        self.sklad2 = Sklad()

    def vstavi(self, vsebina):
        self.sklad1.vstavi(vsebina)

    def prazna(self):
        return self.sklad1.prazen() and self.sklad2.prazen()

    def prelozi(self):
        '''Premakne vse iz sklada1 v sklad2'''
        if self.sklad2.prazen():
            while not self.sklad1.prazen():
                self.sklad2.vstavi(self.sklad1.vrh())
                self.sklad1.odstrani()

    def izberi_element(self):
        if self.sklad1.prazen():
            raise Exception('Skladovnica je prazna')
        if self.sklad2.prazen():
            self.premakni_sklad1_v_sklad2()
        return self.sklad2.vrh()

    def odstrani(self):
        self.prelozi()
        if self.sklad2.prazen():
            raise IndexError('Skladovnica je prazna')
        else:
            self.sklad2.odstrani()


    def zacetek(self):
        self.prelozi()
        if not self.sklad2.prazen():
            return self.sklad2.vrh()
        else:
            raise IndexError('Vrsta je prazna')
        
        
##//JAVA
##public class QueueWithTwoStacks<Item> {
##    private Stack<Item> stack1;    // back of queue
##    private Stack<Item> stack2;    // front of queue
##
##    // create an empty queue
##    public QueueWithTwoStacks() {
##        stack1 = new Stack<Item>();
##        stack2 = new Stack<Item>();
##    }
##
##    // add the item to the queue
##    public void enqueue(Item item) {
##        stack1.push(item);
##    }
##
##    // is the queue empty?
##    public boolean isEmpty() {
##        return stack1.isEmpty() && stack2.isEmpty();
##    }
##
##    // move all items from stack1 to stack2
##    private void moveStack1ToStack2() {
##        while (!stack1.isEmpty())
##            stack2.push(stack1.pop());
##    }
##
##    // return the item least recently added to the queue.
##    public Item peek() {
##        if (isEmpty()) throw new NoSuchElementException("Queue underflow");
##        if (stack2.isEmpty()) moveStack1ToStack2();
##        return stack2.peek();
##    }
##
##    // remove and return the item on the queue least recently added
##    public Item dequeue() {
##        if (isEmpty()) throw new NoSuchElementException("Queue underflow");
##        if (stack2.isEmpty()) moveStack1ToStack2();
##        stack2.pop();
##    }
##
##}
##

