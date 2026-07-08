---
id: UNC@20.15.2@MMLCommand@LST APNEDRXATTR
type: MMLCommand
name: LST APNEDRXATTR（查询APN的终端接入eDRX模式属性）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNEDRXATTR
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- eDRX模式管理
status: active
---

# LST APNEDRXATTR（查询APN的终端接入eDRX模式属性）

## 功能

**适用NF：SMF**

该命令用于查询指定APN的终端接入的eDRX模式。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNEDRXATTR]] · APN的终端接入eDRX模式属性（APNEDRXATTR）

## 使用实例

假如用户需要对APN为“apn1”的终端接入的eDRX模式进行查询，则使用该实例：

```
%%LST APNEDRXATTR: APN="apn1";%%
RETCODE = 0  操作成功

结果如下
------------------------
                       APN名称  =  apn1
              支持eDRX模式开关  =  继承
        下行包缓存数获取优先级  =  从DLBUFFPKTCNT获取
                  下行包缓存数  =  10
            下行包缓存额外时长  =  10
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询APN的终端接入eDRX模式属性（LST-APNEDRXATTR）_32221484.md`
