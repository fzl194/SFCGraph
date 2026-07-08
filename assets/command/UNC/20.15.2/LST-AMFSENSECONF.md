---
id: UNC@20.15.2@MMLCommand@LST AMFSENSECONF
type: MMLCommand
name: LST AMFSENSECONF（查询AMF感知配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AMFSENSECONF
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 感知业务管理
- 感知核查管理
status: active
---

# LST AMFSENSECONF（查询AMF感知配置）

## 功能

**适用NF：AMF**

在部署感知的场景下，通过LST AMFSENSECONF命令查询感知配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/AMFSENSECONF]] · AMF感知配置（AMFSENSECONF）

## 使用实例

若运营商想查询AMF上的感知配置，可以用如下命令：

```
%%LST AMFSENSECONF:;%%
RETCODE = 0  操作成功

结果如下
------------------------
            SFC基站感知能力核查开关  =  DISABLE
SFC基站感知能力核查消息发送周期(min) =  5
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-AMFSENSECONF.md`
