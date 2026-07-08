---
id: UDG@20.15.2@MMLCommand@LST L2TPGROUP
type: MMLCommand
name: LST L2TPGROUP（查询指定L2TP组）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: L2TPGROUP
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- L2TP隧道管理
- L2TP组
status: active
---

# LST L2TPGROUP（查询指定L2TP组）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询本地配置的L2TP信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPID | L2TP组号 | 可选必选说明：可选参数<br>参数含义：指定L2TP组号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～1500。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/L2TPGROUP]] · 指定L2TP组（L2TPGROUP）

## 使用实例

- 假设用户查询所有L2TP组的配置信息：
  ```
  LST L2TPGROUP:;
  ```
  ```

  RETCODE = 0  操作成功。

  L2TP Group 信息
  ---------------
  L2TP组号    隧道鉴权    隧道的域名    隧道本端的名称    隐藏AVP    HELLO报文开关    HELLO报文间隔（秒）    报文重发次数    VPN实例名    是否支持Magic-Number协商    发送窗口上限    初始隧道个数    每条隧道承载的会话个数上限    多LNS的工作模式    第一个LNS IP地址    第一个LNS隧道认证密码    第二个LNS IP地址    第二个LNS隧道认证密码    第三个LNS IP地址    第三个LNS隧道认证密码    第四个LNS IP地址    第四个LNS隧道认证密码    第五个LNS IP地址    第五个LNS隧道认证密码    第六个LNS IP地址    第六个LNS隧道认证密码    DSCP值      是否支持Magic-Number协商    发送窗口上限      初始隧道个数        每条隧道承载的会话个数上限

  1           使能        NULL              NULL              不使能     不使能           0                      3               NULL         不使能                      64              1               32767                         主备             0.0.0.0                *****                 0.0.0.0                *****                0.0.0.0                *****                  0.0.0.0                *****                  0.0.0.0                *****                0.0.0.0                *****                    255                   不使能               64                 1               32767 
  2           使能        example.com       NULL              不使能     不使能           0                      3               NULL         不使能                      64              1               32767                         主备             0.0.0.0                *****                 0.0.0.0                *****                0.0.0.0                *****                  0.0.0.0                *****                  0.0.0.0                *****                0.0.0.0                *****                    255                   不使能               64                 1               32767 
  (结果个数 = 2)
  ---    END
  ```
- 假设用户查询L2TP组1的配置信息：
  ```
  LST L2TPGROUP:GROUPID=1;
  ```
  ```

  RETCODE = 0  操作成功。

  L2TP Group 信息
  ---------------
                    L2TP组号  =  1
                    隧道鉴权  =  使能
                  隧道的域名  =  NULL
              隧道本端的名称  =  NULL
                     隐藏AVP  =  不使能
               HELLO报文开关  =  不使能
         HELLO报文间隔（秒）  =  0
                报文重发次数  =  3
                   VPN实例名  =  NULL
             多LNS的工作模式  =  主备
            第一个LNS IP地址  =  0.0.0.0
       第一个LNS隧道认证密码  =  *****
            第二个LNS IP地址  =  0.0.0.0
       第二个LNS隧道认证密码  =  *****
            第三个LNS IP地址  =  0.0.0.0
       第三个LNS隧道认证密码  =  *****
            第四个LNS IP地址  =  0.0.0.0
       第四个LNS隧道认证密码  =  *****
            第五个LNS IP地址  =  0.0.0.0
       第五个LNS隧道认证密码  =  *****
            第六个LNS IP地址  =  0.0.0.0
       第六个LNS隧道认证密码  =  *****
                      DSCP值  =  255
    是否支持Magic-Number协商  =  不使能
                发送窗口上限  =  64
                初始隧道个数  =  1
  每条隧道承载的会话个数上限  =  32767
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询指定L2TP组（LST-L2TPGROUP）_35373527.md`
