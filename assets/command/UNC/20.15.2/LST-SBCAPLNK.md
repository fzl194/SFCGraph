---
id: UNC@20.15.2@MMLCommand@LST SBCAPLNK
type: MMLCommand
name: LST SBCAPLNK（查询SBc链路）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SBCAPLNK
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- SBc接口管理
- SBc链路
status: active
---

# LST SBCAPLNK（查询SBc链路）

## 功能

**适用网元：MME**

该命令用于查看MME作为客户端的SBc链路配置数据。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LNKINDEX | 链路索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询的SBc链路的索引。<br>数据来源：本端规划<br>取值范围：0~127<br>默认值：无<br>配置原则：此链路索引在系统范围内唯一。 |

## 操作的配置对象

- [SBc链路（SBCAPLNK）](configobject/UNC/20.15.2/SBCAPLNK.md)

## 使用实例

1. 不输入SBc链路索引，查询已经配置的所有SBc链路数据：
  LST SBCAPLNK:;
  ```
  %%LST SBCAPLNK:;%%
  RETCODE = 0  操作成功。

  查询结果如下
  --------------
           链路索引  =  1
         IP地址类型  =  IPv4
          本地地址1  =  10.10.10.15
          本地地址2  =  255.255.255.255
         本地端口号  =  3868
          对端地址1  =  10.10.10.16
          对端地址2  =  255.255.255.255
         对端端口号  =  3868
   SCTP协议参数索引  =  0
   交叉路径是否可用  =  否   
           链路名称  =  To-HSS0
            vpn名称  =  
  UNC
  1 
  (结果个数 = 1)

  ---  END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SBc链路(LST-SBCAPLNK)_26306186.md`
