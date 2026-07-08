---
id: UDG@20.15.2@MMLCommand@DSP TWAMPRESPONDER
type: MMLCommand
name: DSP TWAMPRESPONDER（显示TWAMP响应端状态信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: TWAMPRESPONDER
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPAPM功能管理
- TWAMP
- 查询TWAMP响应端状态
status: active
---

# DSP TWAMPRESPONDER（显示TWAMP响应端状态信息）

## 功能

该命令用于显示TWAMP响应端状态信息。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESPONDERID | 响应端ID | 可选必选说明：可选参数<br>参数含义：该参数用于配置响应端索引。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TWAMPRESPONDER]] · TWAMP响应端（TWAMPRESPONDER）

## 使用实例

查询Responder索引为1的实例：

```
%%DSP TWAMPRESPONDER: RESPONDERID=1;%%
RETCODE = 0  操作成功

结果如下
--------
   Responder索引  =  1
       TWAMP架构  =  full
      本端IP地址  =  10.0.0.0
      对端IP地址  =  192.168.0.0
        状态协商  =  session created
工作模式协商结果  =  no
    会话开始时间  =  1970-01-01 00:00:00
   本端TCP端口号  =  862
   对端TCP端口号  =  1025
   本端UDP端口号  =  65450
   对端UDP端口号  =  1025
差分服务码改变值  =  0
差分服务码初始值  =  0
  接收测量报文数  =  0
  发送测量报文数  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示TWAMP响应端状态信息（DSP-TWAMPRESPONDER）_27262284.md`
