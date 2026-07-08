---
id: UDG@20.15.2@MMLCommand@LST TWAMPSENDER
type: MMLCommand
name: LST TWAMPSENDER（查询TWAMP发送端）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TWAMPSENDER
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPAPM功能管理
- TWAMP
- TWAMP发送端配置
status: active
---

# LST TWAMPSENDER（查询TWAMP发送端）

## 功能

该命令用于查询TWAMP发送端。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CLIENTID | 客户端ID | 可选必选说明：可选参数<br>参数含义：该参数用于配置客户端ID。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~12000。<br>默认值：无<br>配置原则：<br>CLIENTID必须在<br>[**ADD TWAMPCLIENT**](../TWAMP客户端配置/增加TWAMP客户端（ADD TWAMPCLIENT）_27102472.md)<br>已经配置，可以用<br>[**LST TWAMPCLIENT**](../TWAMP客户端配置/查询TWAMP客户端（LST TWAMPCLIENT）_27262286.md)<br>查询。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TWAMPSENDER]] · TWAMP发送端（TWAMPSENDER）

## 使用实例

查询客户端ID为1的发送端实例：

```
%%LST TWAMPSENDER: CLIENTID=1;%%
RETCODE = 0  操作成功

结果如下
--------
    客户端ID  =  1
会话发送类型  =  连续统计
  差分服务码  =  0
    报文类型  =  固定报文长度
    报文长度  =  128
报文填充类型  =  报文随机填充
报文发送周期  =  100
    超时时间  =  5
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-TWAMPSENDER.md`
