---
id: UDG@20.15.2@MMLCommand@LST RSA3072
type: MMLCommand
name: LST RSA3072（查询RSA3072公钥配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: RSA3072
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 业务控制公共配置
- RSA3072公钥配置
status: active
---

# LST RSA3072（查询RSA3072公钥配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询所有的RSA3072配置，支持指定查询某个记录。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RSA3072NAME | RSA3072公钥名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RSA3072公钥配置名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [RSA3072公钥参数（RSA3072）](configobject/UDG/20.15.2/RSA3072.md)

## 使用实例

假如运营商想查看名称为“test”的RSA3072记录：

```
LST RSA3072: RSA3072NAME="test";
```

```

RETCODE = 0  操作成功。

RSA3072公钥参数配置信息
-----------------------
RSA3072公钥名称  =  test
      公钥的N值  =  abcdef
      公钥的E值  =  101010
 头增强前缀开关  =  使能
         国家码  =  123
         网络码  =  456
   公钥配置方式  =  配置公钥
     配置域名称  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询RSA3072公钥配置（LST-RSA3072）_46609224.md`
