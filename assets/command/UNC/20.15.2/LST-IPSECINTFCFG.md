---
id: UNC@20.15.2@MMLCommand@LST IPSECINTFCFG
type: MMLCommand
name: LST IPSECINTFCFG（查询IPsec隧道接口）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IPSECINTFCFG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP安全管理
- 互联网密钥交换
- IPsec接口配置
status: active
---

# LST IPSECINTFCFG（查询IPsec隧道接口）

## 功能

该命令用于查询IPsec隧道。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTERFACENAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：配置接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IPSECINTFCFG]] · 创建IPsec隧道接口（IPSECINTFCFG）

## 使用实例

查询接口名为“Tunnel1/1/1”的安全隧道：

```
LST IPSECINTFCFG:INTERFACENAME="Tunnel1/1/1";
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
        接口名称  =  Tunnel1/1/1
Tunnel口协议类型  =  IP安全
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询IPsec隧道接口（LST-IPSECINTFCFG）_00841437.md`
