---
id: UDG@20.15.2@MMLCommand@LST UPREALMBINDAPN
type: MMLCommand
name: LST UPREALMBINDAPN（查询APN与Diameter Realm关联关系）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UPREALMBINDAPN
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- Diameter管理
- Diameter Realm
- Realm绑定APN
status: active
---

# LST UPREALMBINDAPN（查询APN与Diameter Realm关联关系）

## 功能

**适用NF：UPF**

该命令用于查询Diameter域与APN的绑定关系。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定要与Diameter域绑定的APN实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPREALMBINDAPN]] · APN与Diameter Realm关联关系（UPREALMBINDAPN）

## 使用实例

查询APN isp与Diameter域的绑定关系：

```
LST UPREALMBINDAPN: APN="isp";
```

```

RETCODE = 0  操作成功
APN与Diameter Realm关联关系
---------------------------
                       APN名称  =  isp
                  Diameter应用  =  SWM
   根据IMSI构造归属地Realm开关  =  使能
                       Realm名  =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-UPREALMBINDAPN.md`
