---
id: UDG@20.15.2@MMLCommand@LST IPSECSA
type: MMLCommand
name: LST IPSECSA（查询IPsec安全联盟）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IPSECSA
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP安全管理
- IPsec
- IPsec安全联盟
status: active
---

# LST IPSECSA（查询IPsec安全联盟）

## 功能

该命令用于查询IPsec安全联盟。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SANAME | 安全联盟名称 | 可选必选说明：可选参数<br>参数含义：安全联盟名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。不区分大小写。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IPSECSA]] · IPsec安全联盟（IPSECSA）

## 使用实例

查询IPsec安全联盟：

```
LST IPSECSA: SANAME="1";
```

```

RETCODE = 0  操作成功。

结果如下
--------
            安全联盟名称  =  1
                提议名称  =  1
          入向AH密钥格式  =  无
          出向AH密钥格式  =  无
         入向ESP密钥格式  =  十六进制字符串格式
         出向ESP密钥格式  =  无
  入向AH十六进制认证密钥  =  *****
  出向AH十六进制认证密钥  =  *****
 入向ESP十六进制认证密钥  =  *****
 出向ESP十六进制认证密钥  =  *****
 入向ESP十六进制加密密钥  =  *****
 出向ESP十六进制加密密钥  =  *****
      入向AH安全参数索引  =  256
      出向AH安全参数索引  =  300
     入向ESP安全参数索引  =  NULL
     出向ESP安全参数索引  =  NULL
入向AH字符串格式认证密钥  =  *****
出向AH字符串格式认证密钥  =  *****
   入向ESP字符串格式密钥  =  *****
   出向ESP字符串格式密钥  =  *****
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-IPSECSA.md`
