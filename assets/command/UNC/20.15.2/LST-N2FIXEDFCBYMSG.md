---
id: UNC@20.15.2@MMLCommand@LST N2FIXEDFCBYMSG
type: MMLCommand
name: LST N2FIXEDFCBYMSG（查询指定消息类型固定速率流控信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: N2FIXEDFCBYMSG
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- N2接口固定速率流控管理
status: active
---

# LST N2FIXEDFCBYMSG（查询指定消息类型固定速率流控信息）

## 功能

**适用NF：AMF**

该命令用于查询指定消息类型的固定速率流控信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MSGTYPE | 流控消息类型 | 可选必选说明：可选参数<br>参数含义：该参数用于设置N2接口被流控的消息类型。<br>数据来源：全网规划<br>取值范围：<br>- “NGSETUP（NG Setup Request）”：表示NG Setup Request消息。<br>- “PAGING（Paging）”：表示Paging消息。<br>- “REGISTER（Registration Request）”：表示Registration Request消息。<br>- “SERVICEREQUEST（Service Request）”：表示Service Request消息。<br>- “PATHSWITCH（Path Switch Request）”：表示Path Switch Request消息。<br>- “WPWR（Write-Replace Warning Response）”：表示Write-Replace Warning Response消息。<br>- “PCR（PWS Cancel Response）”：表示PWS Cancel Response消息。<br>- “PRI（PWS Restart Indication）”：表示PWS Restart Indication消息。<br>- “PFI（PWS Failure Indication）”：表示PWS Failure Indication消息。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/N2FIXEDFCBYMSG]] · 指定消息类型固定速率流控信息（N2FIXEDFCBYMSG）

## 使用实例

查询所有流控消息类型流控信息，执行如下命令：

```
%%LST N2FIXEDFCBYMSG:;%%
RETCODE = 0  操作成功

结果如下
--------
流控消息类型                      固定速率流控开关  流控速率门限(个/秒)

NG Setup Request                  开启              500
Paging                            开启              2000
Registration Request              开启              1800
Service Request                   开启              3000
Path Switch Request               开启              8000
Write-Replace Warning Response    开启              1000
PWS Cancel Response               开启              1000
PWS restart Indication            开启              1000
PWS Failure Indication            开启              1000
(结果个数 = 9)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询指定消息类型固定速率流控信息（LST-N2FIXEDFCBYMSG）_96805486.md`
