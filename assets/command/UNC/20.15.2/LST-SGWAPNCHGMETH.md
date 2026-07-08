---
id: UNC@20.15.2@MMLCommand@LST SGWAPNCHGMETH
type: MMLCommand
name: LST SGWAPNCHGMETH（查询SGW APN计费方式）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SGWAPNCHGMETH
command_category: 查询类
applicable_nf:
- SGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- SGW计费控制
- SGW APN计费方式
status: active
---

# LST SGWAPNCHGMETH（查询SGW APN计费方式）

## 功能

**适用NF：SGW-C**

LST SGWAPNCHGMETH命令查询APN下的用户是否产生S-GW话单。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格以及特殊字符：“_”、“#”、“$”、“&”等。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SGWAPNCHGMETH]] · SGW APN计费方式（SGWAPNCHGMETH）

## 使用实例

查询APN实例aa的用户是否打开SGW的离线计费开关，是否生成SGW话单：

```
LST SGWAPNCHGMETH:APN="aa";
```

```

RETCODE = 0  操作成功。

SGW计费方式
-----------
        APN名称  =  aa
APN离线计费开关  =  禁止
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SGW-APN计费方式（LST-SGWAPNCHGMETH）_09896993.md`
