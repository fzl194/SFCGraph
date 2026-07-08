---
id: UNC@20.15.2@MMLCommand@RMV COMPKG
type: MMLCommand
name: RMV COMPKG（移除加载扩展包）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: COMPKG
command_category: 配置类
effect_mode: ''
is_dangerous: true
category_path:
- 平台服务管理
- 操作维护
- 网元管理
status: active
---

# RMV COMPKG（移除加载扩展包）

## 功能

![](移除加载扩展包（RMV COMPKG）_55136287.assets/notice_3.0-zh-cn_2.png)

- 此命令为高危命令，请谨慎使用并联系华为技术支持协助操作。
- 部署了CGPLite服务的系统，如果涉及组件包的移除，组件包移除成功后CGPLite服务会自动重启，正常情况下重启需要一分钟左右的时间，重启期间CGPLite相关业务不可用。

该命令用于删除网元已加载的扩展域的组件包、适配包。

## 注意事项

移除已加载扩展包会导致扩展域功能不可用。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：必选参数。<br>参数含义：网元ID，可以通过<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>获取。<br>取值范围：0～65535<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/COMPKG]] · 扩展包（COMPKG）

## 使用实例

删除网元ID为219的扩展域的组件包、适配包。

```
%%RMV COMPKG: MEID=219;%%
RETCODE = 0 操作成功
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/移除加载扩展包（RMV-COMPKG）_55136287.md`
