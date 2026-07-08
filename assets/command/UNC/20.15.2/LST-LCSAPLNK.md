---
id: UNC@20.15.2@MMLCommand@LST LCSAPLNK
type: MMLCommand
name: LST LCSAPLNK（查询LCSAP链路配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LCSAPLNK
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- LCS
- LCSAP链路配置
status: active
---

# LST LCSAPLNK（查询LCSAP链路配置）

## 功能

**适用网元：MME**

此命令用于查询LCSAP链路配置。

## 注意事项

- 此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LINKIDX | 链路索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定要查询的LCSAP链路索引。<br>取值范围：0～23<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LCSAPLNK]] · LCSAP链路配置（LCSAPLNK）

## 使用实例

查询LCSAP链路设置：

**LST LCSAPLNK:;**

```
%%LST LCSAPLNK:;%%
RETCODE = 0  操作成功。

查询结果如下
--------------
 链路索引  E-SMLC 标识  IP地址类型  本地IP地址1  本地IP地址2      本端端口号  对端IP地址1  对端IP地址2      对端端口号  优先级  SCTP协议参数索引  是否交叉路径可用  链路名称  VPN实例名称

 1         1            IPv4        10.10.10.18  255.255.255.255  9082        10.10.10.20  255.255.255.255  9082        0       0                 否                noname    
UNC

 2         2            IPv4        10.10.10.19  10.10.10.22      9082        10.10.10.21  10.10.10.23      9082        0       0                 是                noname    
UNC

后续仍有报告输出
---    END

%%LST LCSAPLNK:;%%
RETCODE = 0  操作成功。

查询结果如下
--------------
 链路索引  E-SMLC 标识  IP地址类型    本地IP地址1                   本地IP地址2    本端端口号   对端IP地址1                    对端IP地址2     对端端口号  优先级  SCTP协议参数索引  是否交叉路径可用  链路名称  VPN实例名称

 3         1            IPv6          2001:db8:10:19:44:55:10:12    ::              9082        2001:db8:10:19:44:55:10:80     ::              9082        0       0                 否                noname    
UNC

 4         2            IPv6          2001:db8:10:19:44:55:10:13    ::              9082        2001:db8:10:19:44:55:10:81     ::              9082        0       0                 是                noname    
UNC

(结果个数 = 4)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-LCSAPLNK.md`
