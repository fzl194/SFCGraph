---
id: UDG@20.15.2@MMLCommand@LST NSHHEADEN
type: MMLCommand
name: LST NSHHEADEN（查询NSH头增强）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: NSHHEADEN
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 头增强控制
- NSH头增强
- NSH参数
status: active
---

# LST NSHHEADEN（查询NSH头增强）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询NSH头增强全部配置信息，或根据输入名称显示指定NSH头增强的配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NSHNAME | NSH头增强名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置NSH头增强名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| DATATYPE | 数据类型 | 可选必选说明：可选参数<br>参数含义：该参数用于设置NSH头增强的数据类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- MSISDN1：指定插入项的类型为MSISDN。<br>- IMSI1：指定插入项的类型为IMSI。<br>- IMEI1：指定插入项的类型为IMEI。<br>- RAT1：指定插入项的类型为RAT。<br>- ULI1：指定插入项的类型为ULI。<br>- MCC_MNC1：指定插入项的类型为MCC_MNC1。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/NSHHEADEN]] · NSH头增强（NSHHEADEN）

## 使用实例

假如运营商想查看所有的NSH头增强记录：

```
LST NSHHEADEN:;
```

```

RETCODE = 0  操作成功

NSH头增强参数信息
-----------------
     NSH头增强名称  =  nsh
          数据类型  =  MSISDN1
           TAG编码  =  1
需去除的移动国家码  =  NULL
      加密算法标识  =  SHA256
              密钥  =  *****
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-NSHHEADEN.md`
