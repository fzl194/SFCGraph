---
id: UNC@20.15.2@MMLCommand@LST SGSLNK
type: MMLCommand
name: LST SGSLNK（查询SGs链路）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SGSLNK
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- SGSAP
- SGsAP链路管理
status: active
---

# LST SGSLNK（查询SGs链路）

## 功能

**适用网元：MME**

此命令用于查看SGs链路的配置数据。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LNK | 链路索引 | 可选必选说明：可选参数<br>参数含义：待查询链路的索引。<br>取值范围：0~511<br>默认值：无 |
| LSX | 链路集索引 | 可选必选说明：可选参数<br>参数含义：待查询链路所属链路集的索引。<br>取值范围：0~255<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SGSLNK]] · SGs链路（SGSLNK）

## 使用实例

1. 不输入参数，查询系统内所有SGs链路配置数据：
  LST SGSLNK:;
  ```
  %%LST SGSLNK:;%%
  RETCODE = 0  操作成功。

  操作结果如下
  --------------
  链路索引  VPN名称   SGs链路名称  IP地址类型  VLR IP地址1     VLR IP地址2        VLR 端口 本地IP地址1       本地IP地址2      本端端口  链路集索引  SCTP协议参数索引  交叉路径是否可用 

  0         _abc_     VLR8_link1   IPv4        192.168.16.26   255.255.255.255    29118    192.168.16.20     255.255.255.255  29118     0           0                 否               
  1         _abc_     VLR9_link1   IPv4        192.168.16.36   192.168.16.46      29118    192.168.16.30     192.168.16.40    29118     1           0                 否               

  (结果个数 = 2)
  ---    END
  ```
2. 查询链路索引为0的SGs链路配置数据：
  LST SGSLNK: LNK=0;
  ```
  %%LST SGSLNK: LNK=0;%%
  RETCODE = 0  操作成功。

  操作结果如下
  --------------
          链路索引  =  0
           VPN名称  =  _abc_
       SGs链路名称  =  VLR8_link1
        IP地址类型  =  IPv4
       VLR IP地址1  =  192.168.16.26
       VLR IP地址2  =  255.255.255.255
          VLR 端口  =  29118
       本地IP地址1  =  192.168.16.20
       本地IP地址2  =  255.255.255.255
          本端端口  =  29118
        链路集索引  =  0
  SCTP协议参数索引  =  0
  交叉路径是否可用  =  否

  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SGSLNK.md`
