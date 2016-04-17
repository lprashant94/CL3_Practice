package com.example.lpras.memorycalculator;

import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    int prev = 0;

    void function(int operators) {
        EditText Current_textView = (EditText) findViewById(R.id.current);
        TextView res = (TextView) findViewById(R.id.Result);

        Float iResult = null;
        TextView Result_textView = res;
        try {
            iResult = Float.parseFloat(Result_textView.getText().toString());
        } catch (NumberFormatException e) {
            e.printStackTrace();
        }
        Float iCurrent = null;
        try {
            iCurrent = Float.parseFloat(Current_textView.getText().toString());
        } catch (NumberFormatException e) {
            e.printStackTrace();
        }
        if (prev == 1) {

            Result_textView.setText("" + (iResult + iCurrent));

        }
        if (prev == 2) {
            Result_textView.setText("" + (iResult - iCurrent));
        }
        if (prev == 3) {
            Result_textView.setText("" + (iResult * iCurrent));
        }
        if (prev == 4) {
            try {
                Result_textView.setText("" + (iResult / iCurrent));
            } catch (Exception e) {
            }
        }

        if (prev == 0) {
            Result_textView.setText("" + iCurrent);
        }
        prev = operators;
        Current_textView.setText("");

    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
        Button plus = (Button) findViewById(R.id.plus_button);
        Button minus = (Button) findViewById(R.id.minus_button);
        Button mul = (Button) findViewById(R.id.multi_button);
        Button div = (Button) findViewById(R.id.div_button);
        Button clear = (Button) findViewById(R.id.clear_button);
        Button equal = (Button) findViewById(R.id.equal_button);
        Button mem_save = (Button) findViewById(R.id.mem_save);
        Button mem_recall = (Button) findViewById(R.id.mem_recall);
        Button mem_plus = (Button) findViewById(R.id.mem_plus);
        Button mem_minus = (Button) findViewById(R.id.mem_minus);
        Button mem_clear = (Button) findViewById(R.id.mem_clear);
        Button sqrt = (Button) findViewById(R.id.sqrt_button);
        final EditText curr = (EditText) findViewById(R.id.current);
        final TextView res = (TextView) findViewById(R.id.Result);
        final TextView memory = (TextView) findViewById(R.id.Memory);
        sqrt.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Float no = Float.parseFloat(curr.getText().toString());
                Double root = Math.sqrt(no);
                res.setText(root.toString());
            }
        });
        mem_clear.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                memory.setText("");
            }
        });
        mem_save.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                memory.setText(res.getText());
            }
        });
        mem_recall.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                curr.setText(memory.getText());
            }
        });
        mem_plus.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                float a = (float) 0.0;
                float b = (float) 0.0;
                try {
                    a = Float.parseFloat(res.getText().toString());
                } catch (Exception e) {
                    a = (float) 0.0;
                }
                try {
                    b = Float.parseFloat(memory.getText().toString());
                } catch (Exception e) {
                    b = (float) 0.0;
                }
                float val = a + b;
                memory.setText("" + val);
            }
        });
        mem_minus.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                float a = (float) 0.0;
                float b = (float) 0.0;
                try {
                    a = Float.parseFloat(res.getText().toString());
                } catch (Exception e) {
                    a = (float) 0.0;
                }
                try {
                    b = Float.parseFloat(memory.getText().toString());
                } catch (Exception e) {
                    b = (float) 0.0;
                }
                float val = b - a;
                memory.setText("" + val);
            }
        });
        equal.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                function(0);
            }
        });


        clear.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                res.setText("0");
                curr.setText("");

            }
        });


        assert plus != null;
        plus.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                function(1);

            }
        });
        minus.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                function(2);
            }
        });
        mul.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                function(3);

            }
        });
        div.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                function(4);
            }
        });
        FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                        .setAction("Action", null).show();
            }
        });
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}
