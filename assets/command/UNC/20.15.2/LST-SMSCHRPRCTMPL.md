---
id: UNC@20.15.2@MMLCommand@LST SMSCHRPRCTMPL
type: MMLCommand
name: LST SMSCHRPRCTMPL（查询SMS CHR流程控制模板）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMSCHRPRCTMPL
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- CHR管理
status: active
---

# LST SMSCHRPRCTMPL（查询SMS CHR流程控制模板）

## 功能

**适用NF：SMSF**

该命令用于查询SMS CHR流程控制模板。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TMPLIDX | 流程控制模板索引 | 可选必选说明：可选参数<br>参数含义：该参数用于表示流程控制模板索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~127。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMSCHRPRCTMPL]] · SMS CHR流程控制模板（SMSCHRPRCTMPL）

## 使用实例

运营商希望查询SMS CHR流程控制模板，执行如下命令 ：

```
LST SMSCHRPRCTMPL:;
%%LST SMSCHRPRCTMPL:;%%
RETCODE = 0  操作成功

结果如下：
------------------------
流程控制模板索引 =  1
短信CHR失败流程上报选项  =  其他流程需要上报CHR单据
       
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SMS-CHR流程控制模板（LST-SMSCHRPRCTMPL）_04041269.md`
