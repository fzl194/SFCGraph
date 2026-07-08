---
id: UDG@20.15.2@MMLCommand@DSP SOFTWARE
type: MMLCommand
name: DSP SOFTWARE（显示软件仓软件）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SOFTWARE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务平台功能管理
- 系统管理
- 系统维护
- 软件仓软件
status: active
---

# DSP SOFTWARE（显示软件仓软件）

## 功能

该命令用于显示软件仓软件的信息。

## 注意事项

该指令只在VNFP侧提供。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VNFCTYPE | VNFC类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VNFC类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～39。<br>默认值：无<br>配置原则：当不输入时显示所有的VNFC的信息。 |

## 操作的配置对象

- [下载软件仓软件（SOFTWARE）](configobject/UDG/20.15.2/SOFTWARE.md)

## 使用实例

显示软件仓软件信息，请执行以下命令：

```
DSP SOFTWARE:VNFCTYPE="VNRS_VNFC";
```

```
RETCODE = 0  操作成功 
 
结果如下: 
------------------------- 
VNFC类型     包类型    版本应用类型      版本类型      版本号            基础版本号       CPU架构类型

VNRS_VNFC    版本包    BaseApp           基础版本      V100R005C10B100   V100R005C10B100    X86
VNRS_VNFC    版本包    BaseApp           基础版本      V100R005C10B200   V100R005C10B200    X86
VNRS_VNFC    版本包    BaseApp           基础版本      V100R005C10B300   V100R005C10B300    X86

(结果个数 = 3) 
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示软件仓软件（DSP-SOFTWARE）_59036808.md`
