---
id: UNC@20.15.2@MMLCommand@LST GLOBALWIFILTEHO
type: MMLCommand
name: LST GLOBALWIFILTEHO（查询全局E-UTRAN和WLAN互操作控制属性）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GLOBALWIFILTEHO
command_category: 查询类
applicable_nf:
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- E-UTRAN和WLAN互操作控制
- 全局E-UTRAN和WLAN互操作控制
status: active
---

# LST GLOBALWIFILTEHO（查询全局E-UTRAN和WLAN互操作控制属性）

## 功能

**适用NF：PGW-C**

该命令用于查询全局E-UTRAN和WLAN互操作控制属性。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GLOBALWIFILTEHO]] · 全局E-UTRAN和WLAN互操作控制属性（GLOBALWIFILTEHO）

## 使用实例

查询全局E-UTRAN和WLAN互操作属性：

```
%%LST GLOBALWIFILTEHO:;%%
RETCODE = 0  操作成功

结果如下
--------
忽略信令消息中HI开关  =  不使能
     S2b接口切换开关  =  不使能
     S2a接口切换开关  =  不使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-GLOBALWIFILTEHO.md`
