---
id: UNC@20.15.2@MMLCommand@SET BASESOFTPARA
type: MMLCommand
name: SET BASESOFTPARA（设置基础软件参数配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: BASESOFTPARA
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 基础软件参数管理
status: active
---

# SET BASESOFTPARA（设置基础软件参数配置）

## 功能

该命令用于设置基础软件参数配置，基础软件参数配置主要用于在日常的数据配置与调试过程中，由于周边互通网元的特殊要求、标准协议实现方式不同或运营商网络参数特殊要求等而引起的需要专门配置参数的场景，参数设置直接影响到系统的业务处理方式。

## 注意事项

- 该命令执行后立即生效。
- 使用基础软件参数配置功能需要先将基础软参参数的类型和索引注册到白名单中。
- 基础软件参数配置后，记录可以修改更新但是不能被删除。
- 使用前，请检查资料版本与软件版本是否一致，如果不一致，请联系华为技术支持获取与软件版本对应的资料。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PARATYPE | 基础软件参数类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定基础软件参数的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DWORD：双字类型。<br>- STRING：字符串类型。<br>默认值：无 |
| PARAINDEX | 基础软件参数索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定基础软件参数的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：无 |
| VALUE | 基础软件参数内容 | 可选必选说明：必选参数<br>参数含义：该参数用于指定基础软件参数的内容。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [基础软件参数配置（BASESOFTPARA）](configobject/UNC/20.15.2/BASESOFTPARA.md)

## 使用实例

设置基础软件参数配置，参数类型是双字类型，参数索引是1，内容值是1：

```
SET BASESOFTPARA:PARATYPE=DWORD, PARAINDEX=1,VALUE="1"
,SERVICEINSTANCE="vnfc"
;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置基础软件参数配置（SET-BASESOFTPARA）_59103695.md`
