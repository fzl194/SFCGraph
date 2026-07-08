---
id: UNC@20.15.2@MMLCommand@LST COMPKG
type: MMLCommand
name: LST COMPKG（查询加载扩展包）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: COMPKG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 网元管理
status: active
---

# LST COMPKG（查询加载扩展包）

## 功能

该命令可以查询已加载的扩展域组件包名称、组件版本、当前组件包状态信息。

## 注意事项

无。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：必选参数。<br>参数含义：网元ID，可以通过<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>获取。<br>取值范围：0～65535<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [扩展包（COMPKG）](configobject/UNC/20.15.2/COMPKG.md)

## 使用实例

查询网元ID为219的网元信息。

```
%%LST COMPKG: MEID=219;%%
RETCODE = 0 操作成功

操作结果如下
------------
网元类型  =  APPTYPE
网元ID    =  219
组件名称  =  APP_TYPE_XXX_V100200300400
组件版本  =  V100200300400
组件状态  =  正常
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询加载扩展包（LST-COMPKG）_55136286.md`
