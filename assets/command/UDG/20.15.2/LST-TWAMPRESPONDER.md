---
id: UDG@20.15.2@MMLCommand@LST TWAMPRESPONDER
type: MMLCommand
name: LST TWAMPRESPONDER（查询TWAMP响应端）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TWAMPRESPONDER
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPAPM功能管理
- TWAMP
- TWAMP响应端配置
status: active
---

# LST TWAMPRESPONDER（查询TWAMP响应端）

## 功能

该命令用于查询TWAMP响应端。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESPONDERID | 响应端索引 | 可选必选说明：可选参数<br>参数含义：该参数用于配置响应端索引。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@TWAMPRESPONDER]] · TWAMP响应端（TWAMPRESPONDER）

## 使用实例

查询响应端索引为1的实例：

```
%%LST TWAMPRESPONDER: RESPONDERID=1;%%
RETCODE = 0  操作成功

结果如下
--------
  响应端索引  =  1
  地址族类型  =  IPV4
   TWAMP架构  =  FULL
本端IPV4地址  =  10.0.0.0
协商等待时间  =  900
测试等待时间  =  900
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-TWAMPRESPONDER.md`
