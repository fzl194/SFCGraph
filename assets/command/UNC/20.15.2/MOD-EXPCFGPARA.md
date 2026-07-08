---
id: UNC@20.15.2@MMLCommand@MOD EXPCFGPARA
type: MMLCommand
name: MOD EXPCFGPARA（修改MML导入导出密钥）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: EXPCFGPARA
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 配置维护
- 配置数据
status: active
---

# MOD EXPCFGPARA（修改MML导入导出密钥）

## 功能

该命令用于MML导入导出之前，下发对DB表中密码字段进行加解密的用户密钥。

## 注意事项

该命令执行后立即生效，且针对指定的VNFC独立生效。加密导出数据前，建议对每个VNFC都运行该命令。

如果执行EXP MML命令导出带密码字段的配置时，参数PWDKEY则必须填写。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PWDKEY | 用户配置密钥 | 可选必选说明：可选参数<br>参数含义：MML导入导出用户配置密钥。<br>数据来源：本端规划<br>取值范围：密码类型，输入长度范围为6～16。当前仅支持明文密钥输入。<br>默认值：无<br>配置原则：<br>- 密码必须包含数字、大写字母、小写字母、特殊字符中至少两种字符的组合。<br>- 输入单空格或不输入将删除该参数已有配置项。 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/EXPCFGPARA]] · MML导入导出密钥（EXPCFGPARA）

## 使用实例

下发MML导入导出用户密钥：

```
MOD EXPCFGPARA:PWDKEY="*****"
,SERVICEINSTANCE="vnfc"
;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-EXPCFGPARA.md`
