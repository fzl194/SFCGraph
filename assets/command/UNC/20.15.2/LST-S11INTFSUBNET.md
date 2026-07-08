---
id: UNC@20.15.2@MMLCommand@LST S11INTFSUBNET
type: MMLCommand
name: LST S11INTFSUBNET（查询S11接口子网配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: S11INTFSUBNET
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- S11接口管理
- S-GWIP地址配置
status: active
---

# LST S11INTFSUBNET（查询S11接口子网配置）

## 功能

**适用网元：MME**

此命令用于查询S11或S11-U接口的子网配置。

## 注意事项

- 无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LNKIDX | 链路关联索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本对端IP地址关联索引。<br>取值范围：0~65534<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/S11INTFSUBNET]] · S11接口子网配置（S11INTFSUBNET）

## 使用实例

1. 查询关联索引为0的S11接口子网配置，可以用如下命令：
  LST S11INTFSUBNET: LNKIDX=0;
  ```
  %%LST S11INTFSUBNET: LNKIDX=0;%%
  RETCODE = 0  操作成功。

  操作结果如下
  ------------
  链路关联索引  =  0
    远端实例ID  =  12
   S11接口类型  =  S11接口
    IP地址类型  =  IPV4
  本端IPV4地址  =  10.2.3.4
  对端IPV4地址  =  10.2.3.6
      IPV4掩码  =  255.255.255.0
  本端IPV6地址  =  ::
  对端IPV6地址  =  ::
      IPV6掩码  =  0
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询S11接口子网配置-(LST-S11INTFSUBNET)_19337754.md`
