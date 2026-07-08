---
id: UNC@20.15.2@MMLCommand@LST PAEPORTGATEWAY
type: MMLCommand
name: LST PAEPORTGATEWAY（查询网关转发地址）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PAEPORTGATEWAY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 配置
status: active
---

# LST PAEPORTGATEWAY（查询网关转发地址）

## 功能

该命令用于查询内联口的网关转发地址信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/PAEPORTGATEWAY]] · PAE端口网关信息（PAEPORTGATEWAY）

## 使用实例

显示内联口的网关地址信息：

```
%%LST PAEPORTGATEWAY:;%%
RETCODE = 0  操作成功

结果如下
--------
网段索引  平面ID  IP地址类型  网关IPv4地址  IPv4地址掩码  网关IPv6地址  IPv6地址前缀  描述  

1         0       IPv4        192.168.2.3   255.255.0.0   ::            0             NULL  
2         0       IPv4        172.16.52.1   255.255.0.0   ::            0             NULL  
3         0       IPv4        172.28.78.8   255.255.0.0   ::            0             NULL  
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询网关转发地址（LST-PAEPORTGATEWAY）_48164178.md`
