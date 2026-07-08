---
id: UNC@20.15.2@MMLCommand@LST NRFNFTIMER
type: MMLCommand
name: LST NRFNFTIMER（查询指定NF在NRF上的时长信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFNFTIMER
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- 定时器参数
status: active
---

# LST NRFNFTIMER（查询指定NF在NRF上的时长信息）

## 功能

**适用NF：NRF**

该命令用于查询指定NF在NRF上的时长信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示NF实例标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~36。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFNFTIMER]] · 指定NF在NRF上的时长信息（NRFNFTIMER）

## 使用实例

在NRF上查询实例标识为"88888888-6666-1234-5678-123456789ABC"的时长信息，执行如下命令。

```
LST NRFNFTIMER: NFINSTANCEID="88888888-4444-1234-5678-123456789ABC";
%%LST NRFNFTIMER: NFINSTANCEID="88888888-4444-1234-5678-123456789ABC";%%
RETCODE = 0  操作成功

结果如下
------------
	      NF实例标识  =  88888888-4444-1234-5678-123456789abc
服务发现缓存有效时长(秒)  =  120
        订阅有效时长(秒)  =  120
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询指定NF在NRF上的时长信息（LST-NRFNFTIMER）_07489930.md`
