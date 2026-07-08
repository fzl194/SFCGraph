---
id: UNC@20.15.2@MMLCommand@LST IUPFAPNDPMODE
type: MMLCommand
name: LST IUPFAPNDPMODE（查询I-UPF在特定园区专用APN下的部署模式配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IUPFAPNDPMODE
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- I-UPF部署策略
- APN粒度的I-UPF部署模式
status: active
---

# LST IUPFAPNDPMODE（查询I-UPF在特定园区专用APN下的部署模式配置）

## 功能

**适用NF：SMF**

该命令用于查询I-UPF在特定园区专用APN下的部署模式配置，对非ULCL场景生效。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示APN名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数取值应与ADD APN命令中参数“APN”保持一致。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IUPFAPNDPMODE]] · I-UPF在特定园区专用APN下的部署模式配置（IUPFAPNDPMODE）

## 使用实例

查询APN为huawei.com的IUPF部署模式配置：

```
%%LST IUPFAPNDPMODE: APN="huawei.com";%%
            RETCODE = 0  操作成功

            结果如下
            --------
            APN  =  huawei.com
            5G下的IUPF部署模式  =  禁止插入IUPF
            5G禁止IUPF插入时返回的失败NAS原因值 = INSUFFICIENT_RESOURCES_FOR_SPECIFIC_SLICE_AND_DNN
            (结果个数 = 1)

            ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-IUPFAPNDPMODE.md`
