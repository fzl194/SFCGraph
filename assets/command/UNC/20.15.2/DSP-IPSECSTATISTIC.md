---
id: UNC@20.15.2@MMLCommand@DSP IPSECSTATISTIC
type: MMLCommand
name: DSP IPSECSTATISTIC（查询IPsec统计信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: IPSECSTATISTIC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- IPsec调测
- IPsec诊断信息
- IPsec处理报文统计信息
status: active
---

# DSP IPSECSTATISTIC（查询IPsec统计信息）

## 功能

该命令用于查询IPsec处理报文统计信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SANAME | 安全联盟名称 | 可选必选说明：可选参数<br>参数含义：安全联盟名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。不区分大小写。<br>默认值：无 |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用DSP RU命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IPSECSTATISTIC]] · IPsec统计信息（IPSECSTATISTIC）

## 使用实例

查询IPsec处理报文统计信息：

```
DSP IPSECSTATISTIC: SANAME="1";
```

```

RETCODE = 0  操作成功。

结果如下
--------
              入向IPv6安全报文计数  =  0
              出向IPv6安全报文计数  =  0
                入向IPv6安全字节数  =  0
                出向IPv6安全字节数  =  0
          入向IPv6丢弃安全报文计数  =  0
          出向IPv6丢弃安全报文计数  =  0
因为内存处理问题导致的IPv6报文丢弃  =  0
  因为查找不到SA导致的IPv6报文丢弃  =  0
    因为队列已满导致的IPv6报文丢弃  =  0
    因为认证失败导致的IPv6报文丢弃  =  0
因为报文长度错误导致的IPv6报文丢弃  =  0
    因为报文重放导致的IPv6报文丢弃  =  0
    因为报文超长导致的IPv6报文丢弃  =  0
      因为SA无效导致的IPv6报文丢弃  =  0
        丢弃的正常入向IPv6报文计数  =  0
        丢弃的正常出向IPv6报文计数  =  0
              入向IPv4安全报文计数  =  0
              出向IPv4安全报文计数  =  0
                入向IPv4安全字节数  =  0
                出向IPv4安全字节数  =  0
          入向IPv4丢弃安全报文计数  =  0
          出向IPv4丢弃安全报文计数  =  0
因为内存处理问题导致的IPv4报文丢弃  =  0
  因为查找不到SA导致的IPv4报文丢弃  =  0
    因为队列已满导致的IPv4报文丢弃  =  0
    因为认证失败导致的IPv4报文丢弃  =  0
因为报文长度错误导致的IPv4报文丢弃  =  0
    因为报文重放导致的IPv4报文丢弃  =  0
    因为报文超长导致的IPv4报文丢弃  =  0
      因为SA无效导致的IPv4报文丢弃  =  0
        丢弃的正常入向IPv4报文计数  =  0
        丢弃的正常出向IPv4报文计数  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询IPsec统计信息（DSP-IPSECSTATISTIC）_00841381.md`
