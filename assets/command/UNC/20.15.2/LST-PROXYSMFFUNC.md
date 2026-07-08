---
id: UNC@20.15.2@MMLCommand@LST PROXYSMFFUNC
type: MMLCommand
name: LST PROXYSMFFUNC（查询proxy SMF功能配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PROXYSMFFUNC
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- Proxy SGW_SMF管理
- Proxy SMF功能管理
status: active
---

# LST PROXYSMFFUNC（查询proxy SMF功能配置）

## 功能

**适用NF：SMF**

该命令用于查询PROXYSMFFUNC参数。

## 注意事项

该命令参数NRFPRISW已弃用。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/PROXYSMFFUNC]] · proxy SMF功能配置（PROXYSMFFUNC）

## 使用实例

查询proxy SMF控制配置。

```
%%LST PROXYSMFFUNC:;%%
RETCODE = 0 操作成功
结果如下
--------
                               归属地SMF实例标识的查询 = IMSI优先
                   是否优先选择支持互操作能力的归属地SMF =  开启
             是否选择相同DNN和不同S-NSSAI会话的归属地SMF = 关闭
                            是否优先向NRF发现归属地SMF = 关闭
                          是否根据接入类型过滤归属地SMF = 关闭
                                            控制类型 = 允许
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PROXYSMFFUNC.md`
