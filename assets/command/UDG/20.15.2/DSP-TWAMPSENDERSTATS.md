---
id: UDG@20.15.2@MMLCommand@DSP TWAMPSENDERSTATS
type: MMLCommand
name: DSP TWAMPSENDERSTATS（显示TWAMP发送端详细信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: TWAMPSENDERSTATS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPAPM功能管理
- TWAMP
- 查询TWAMP发送端状态
status: active
---

# DSP TWAMPSENDERSTATS（显示TWAMP发送端详细信息）

## 功能

该命令用于显示TWAMP发送端详细信息。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CLIENTID | 客户端ID | 可选必选说明：可选参数<br>参数含义：该参数用于配置客户端ID。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~12000。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TWAMPSENDERSTATS]] · TWAMP发送端详细信息（TWAMPSENDERSTATS）

## 使用实例

查询客户端ID为1的发送端实例：

```
%%DSP TWAMPSENDERSTATS: CLIENTID=1;%%
RETCODE = 0  操作成功
 
结果如下
--------
    客户端ID  =  1
      源地址  =  10.0.0.0
    目的地址  =  192.168.0.0
      丢包率  =  0
    双向时延  =  1
发送方向抖动  =  0
接收方向抖动  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示TWAMP发送端详细信息（DSP-TWAMPSENDERSTATS）_73142133.md`
