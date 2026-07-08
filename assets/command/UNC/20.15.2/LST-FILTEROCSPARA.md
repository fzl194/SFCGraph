---
id: UNC@20.15.2@MMLCommand@LST FILTEROCSPARA
type: MMLCommand
name: LST FILTEROCSPARA（查询需要过滤掉的OCS实例信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: FILTEROCSPARA
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 需要过滤掉的OCS实例信息
status: active
---

# LST FILTEROCSPARA（查询需要过滤掉的OCS实例信息）

## 功能

**适用NF：NCG**

该命令用于查询需要过滤掉的OCS实例信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FILTERID | OCS过滤标识 | 可选必选说明：可选参数<br>参数含义：该参数表示过滤的OCS标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~40。字符串类型，输入长度范围是1~40。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）、下划线（_）组成。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/FILTEROCSPARA]] · 需要过滤掉的OCS实例信息（FILTEROCSPARA）

## 使用实例

查询所有过滤掉的OCS实例信息：

```
LST FILTEROCSPARA:;
%%LST FILTEROCSPARA:;%%
RETCODE = 0  操作成功

结果如下
------------------------
OCS过滤标识  =  ocsid001
  NF实例ID  =  88888888-4444-1234-5678-123456789ABC
业务实例ID  =  service_instance_0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-FILTEROCSPARA.md`
