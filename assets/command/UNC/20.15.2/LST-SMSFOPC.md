---
id: UNC@20.15.2@MMLCommand@LST SMSFOPC
type: MMLCommand
name: LST SMSFOPC（查询SMSF本局信令点）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMSFOPC
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SMSF管理
- SMSFOPC本局信令点
status: active
---

# LST SMSFOPC（查询SMSF本局信令点）

## 功能

**适用NF：SMSF**

该命令用于查询配置的SMSFOPC本局信令点。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OPX | SMSF信令点索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SMSF本局信令点索引。<br>数据来源：本端规划<br>取值范围：1～10<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMSFOPC]] · SMSF本局信令点（SMSFOPC）

## 使用实例

查询已经配置的所有的SMSFOPC记录。

```
%%LST SMSFOPC:;%%
RETCODE = 0  操作成功 
The result is as follows 
------------------------ 
SMSF信令点索引  网络指示语     本局信令点编码 本局SMSF号     本局信令点名  是否主用信令点

1               国内网         0x17701  861390211101          noname         YES
2               国际网         0x1      861                   noname         NO
(结果个数 = 2)  
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SMSFOPC.md`
