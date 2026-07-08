---
id: UNC@20.15.2@MMLCommand@SET UPGRADEWATCH
type: MMLCommand
name: SET UPGRADEWATCH（设置升级观察期）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: UPGRADEWATCH
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 升级补丁管理
- 观察期管理
status: active
---

# SET UPGRADEWATCH（设置升级观察期）

## 功能

![](设置升级观察期(SET UPGRADEWATCH)_13530392.assets/notice_3.0-zh-cn_2.png)

执行此命令会延长或缩短所有网元升级观察期数据，同时在升级或者备份恢复任务过程中勿执行此命令，请谨慎操作。

该命令用于设置所有网元升级观察期天数。

## 注意事项

无。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| CFGTYPE | 配置类型 | 可选必选说明：必选参数<br>参数含义：用于设置网元的升级观察期类型。<br>取值范围：<br>- PERMANENT(永久)<br>- SPECIFIED(指定)<br>默认值：SPECIFIED(指定)<br>配置原则：无。 |
| DAYS | 观察期天数 | 可选必选说明：该参数在<br>“CFGTYPE”<br>配置为<br>“SPECIFIED(指定)”<br>时为条件必选参数。<br>参数含义：用于设置升级观察期的天数。<br>取值范围：1~180<br>默认值：14<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UPGRADEWATCH]] · 升级观察期（UPGRADEWATCH）

## 使用实例

设置升级观察期天数为180天。

```
%%SET UPGRADEWATCH: CFGTYPE=SPECIFIED, DAYS=180;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置升级观察期(SET-UPGRADEWATCH)_13530392.md`
