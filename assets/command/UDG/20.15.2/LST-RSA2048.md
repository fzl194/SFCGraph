---
id: UDG@20.15.2@MMLCommand@LST RSA2048
type: MMLCommand
name: LST RSA2048（查询RSA2048公钥配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: RSA2048
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
- RSA2048公钥配置
status: active
---

# LST RSA2048（查询RSA2048公钥配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询所有的RSA2048配置，支持指定查询某个记录。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RSA2048NAME | RSA2048公钥名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RSA2048公钥配置名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RSA2048]] · RSA2048公钥参数（RSA2048）

## 使用实例

假如运营商想查看名称为“test”的RSA2048记录：

```
LST RSA2048: RSA2048NAME="test";
```

```

RETCODE = 0  操作成功。

RSA2048公钥参数配置信息
-----------------------
RSA2048公钥名称  =  test
      公钥的N值  =  abcdef
      公钥的E值  =  101010
 头增强前缀开关  =  使能
         国家码  =  123
         网络码  =  456
   公钥配置方式  =  配置公钥
RSA证书文件索引  =  0
     配置域名称  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询RSA2048公钥配置（LST-RSA2048）_82837579.md`
