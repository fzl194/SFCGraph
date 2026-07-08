---
id: UNC@20.15.2@MMLCommand@LST DATACHKPOLICY
type: MMLCommand
name: LST DATACHKPOLICY（查询APP配置数据检查功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DATACHKPOLICY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 配置管理
- 配置检查
status: active
---

# LST DATACHKPOLICY（查询APP配置数据检查功能）

## 功能

该命令用于查询APP配置数据检查功能使能信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识，0表示VNFP。 |

## 操作的配置对象

- [APP配置数据检查功能（DATACHKPOLICY）](configobject/UNC/20.15.2/DATACHKPOLICY.md)

## 使用实例

查询APP配置数据检查功能：

```
LST DATACHKPOLICY:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
---------
自动检查开关  =  开
    检查时间  =  02:30:00
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询APP配置数据检查功能（LST-DATACHKPOLICY）_59103394.md`
