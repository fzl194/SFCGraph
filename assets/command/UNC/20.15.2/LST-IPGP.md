---
id: UNC@20.15.2@MMLCommand@LST IPGP
type: MMLCommand
name: LST IPGP（查询IP群组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IPGP
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
- IP群组配置
status: active
---

# LST IPGP（查询IP群组）

## 功能

**适用网元：SGSN、MME**

该命令用于查询IP群组配置。

## 注意事项

如果有输入参数，则显示与输入参数匹配的IP群组配置记录；如果没有输入参数，则显示所有IP群组配置记录。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPGPID | IP群组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IP群组标识。<br>数据来源：本端规划<br>取值范围：1-255<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IPGP]] · IP群组（IPGP）

## 使用实例

1. 查询IPGPID为1的IP群组配置信息，配置格式为：
  LST IPGP: IPGPID=1;
  ```
  %%
  LST IPGP: IPGPID=1;
  %%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------
  IP群组标识  =  1
    群组名称  =  DCNR_SGW
  (结果个数 = 1)

  ---    END
  ```
2. 查询所有的IP群组配置信息，配置格式为：
  LST IPGP:;
  ```
  %%LST IPGP:;%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------
  IP群组标识  群组名称
  1           DCNR_SGW
  2           MME_SGW
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-IPGP.md`
