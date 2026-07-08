---
id: UNC@20.15.2@MMLCommand@LST IPV6GPMEM
type: MMLCommand
name: LST IPV6GPMEM（查询IPv6群组成员）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IPV6GPMEM
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- IP群组管理
- IP群组成员配置
status: active
---

# LST IPV6GPMEM（查询IPv6群组成员）

## 功能

**适用网元：SGSN、MME**

该命令用于查询IP群组成员配置。

## 注意事项

如果有输入参数，则显示与输入参数匹配的IP群组成员配置记录；如果没有输入参数，则显示所有IP群组成员配置记录。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPGPID | IP群组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IP群组标识。<br>前提条件：“IP群组标识”已经通过<br>[**ADD IPGP**](../IP群组配置/增加IP群组(ADD IPGP)_18995796.md)<br>配置。<br>数据来源：本端规划<br>取值范围：1-255<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IPV6GPMEM]] · IPv6群组成员（IPV6GPMEM）

## 使用实例

查询IPv6群组成员配置：

LST IPV6GPMEM:;

```
%%LST IPV6GPMEM:;%%
RETCODE = 0  操作成功。

操作结果如下
------------
          IP群组标识  =  1
            IPv6地址  =  
2001:db8::

    IPV6地址前缀长度  =  64
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-IPV6GPMEM.md`
