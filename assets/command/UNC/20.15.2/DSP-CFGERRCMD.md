---
id: UNC@20.15.2@MMLCommand@DSP CFGERRCMD
type: MMLCommand
name: DSP CFGERRCMD（显示CFG方式配置恢复的失败信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: CFGERRCMD
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 配置维护
- 配置恢复失败命令
status: active
---

# DSP CFGERRCMD（显示CFG方式配置恢复的失败信息）

## 功能

该命令用于显示CFG方式配置恢复的失败信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CFGERRCMD]] · CFG方式配置恢复的失败信息（CFGERRCMD）

## 使用实例

显示CFG方式配置恢复的失败信息：

```
DSP CFGERRCMD:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
----------
时间                 原因       行号    视图     命令

2017-07-25 15:44:55  执行失败   30      aaa      local-user _@1 service-type http
2017-07-25 15:44:55  执行失败   31      aaa      local-user _@2 service-type http
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示CFG方式配置恢复的失败信息（DSP-CFGERRCMD）_59103943.md`
