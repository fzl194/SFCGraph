---
id: UNC@20.15.2@MMLCommand@LST BASESOFTPARA
type: MMLCommand
name: LST BASESOFTPARA（查询基础软件参数配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: BASESOFTPARA
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 基础软件参数管理
status: active
---

# LST BASESOFTPARA（查询基础软件参数配置）

## 功能

该命令用于查询基础软件参数配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PARATYPE | 基础软件参数类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定基础软件参数的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DWORD：双字类型。<br>- STRING：字符串类型。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/BASESOFTPARA]] · 基础软件参数配置（BASESOFTPARA）

## 使用实例

查询基础软件参数配置信息：

```
LST BASESOFTPARA:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
-------------------------
 基础软件参数类型  =  双字
 基础软件参数索引  =  1
 基础软件参数内容  =  1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-BASESOFTPARA.md`
