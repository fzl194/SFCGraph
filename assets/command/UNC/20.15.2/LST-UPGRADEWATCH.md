---
id: UNC@20.15.2@MMLCommand@LST UPGRADEWATCH
type: MMLCommand
name: LST UPGRADEWATCH（查询升级观察期）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UPGRADEWATCH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 升级补丁管理
- 观察期管理
status: active
---

# LST UPGRADEWATCH（查询升级观察期）

## 功能

该命令用于查询所有网元升级观察期数据。

## 注意事项

查询到的升级观察期数据对所有网元有效，不区分网元。

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/UPGRADEWATCH]] · 升级观察期（UPGRADEWATCH）

## 使用实例

查询升级观察期剩余天数和天数设置。

```
%%LST UPGRADEWATCH:;%%
RETCODE = 0  操作成功

升级观察期信息
--------------
      剩余天数  =  0
观察期天数设置  =  180
    观察期类型  =  USCDB插件升级
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询升级观察期(LST-UPGRADEWATCH)_58490247.md`
