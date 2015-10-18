/**
 * Created by vamseek on 10/1/15.
 */
document.writeln("Hello mama");

var myFirstObj = {
    name: 'Vineel',
    change: function()
    {
        this.name += 'Pullipudi';
        document.writeln(this.name);
    }
};


myFirstObj.name2 = "Vamsee";
myFirstObj.change2 = function()
{
    this.name2 += 'Pullipudi2';
    document.writeln(this.name2);
};

//myFirstObj.change2();



function MyFirstFunc() {

  var name = 'VineelFunc';
    return {

        change: function(){
            name += 'PullipudiFunction';
            document.writeln(name);
        }
    };
}

Function.prototype.method = function (name, func) {
    this.prototype[name] = func;
    return this;
};

Function.method('inherits', function (Parent) {
    this.prototype = new Parent( );
    return this;
});


var x = new MyFirstFunc();
x.change();


function MyFirstFunc2() {

    this.name = 'VineelFunc';

}

MyFirstFunc2.method("change2", function(iname)
{
   document.writeln(iname + " " + this.name);
});

MyFirstFunc2.prototype.change3 = function(){ document.writeln("vammooo");};


var y = new MyFirstFunc2();
y.change2("Vamsee");
y.change3();

