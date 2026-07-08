---
id: UNC@20.15.2@MMLCommand@LST RCAPLNK
type: MMLCommand
name: LST RCAPLNK（查询注册中心链路）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RCAPLNK
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- 注册中心管理
status: active
---

# LST RCAPLNK（查询注册中心链路）

## 功能

**适用NF：SMSF**

此命令用于查询注册中心链路配置。

## 注意事项

无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LNK | 链路索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定链路的索引。该参数用来在系统范围内部唯一标识一条Rcenter链路。<br>数据来源：整网规划<br>取值范围：0~1023<br>默认值：无 |
| LSX | 链路集索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定所属链路集的索引。<br>数据来源：整网规划<br>取值范围：0~255<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RCAPLNK]] · 注册中心链路（RCAPLNK）

## 使用实例

1. 查询链路索引为0的注册中心链路配置，可以用如下命令：
  LST RCAPLNK: LNK=0;
  ```
  %%LST RCAPLNK: LNK=0;%%
  RETCODE = 0  操作成功。

  操作结果如下
  ------------
          链路索引  =  0
      RCAP链路名称  =  huawei
        IP地址类型  =  IPV4
    RCAP IPv4地址1  =  10.2.3.4
    RCAP IPv4地址2  =  10.2.3.6
    RCAP IPv6地址1  =  ::
    RCAP IPv6地址2  =  ::
          RCAP端口  =  29118
     本地IPv4地址1  =  192.168.37.128
     本地IPv4地址1  =  192.168.37.129
     本地IPv6地址1  =  ::
     本地IPv6地址1  =  ::
          本端端口  =  29118
        链路集索引  =  0
  SCTP协议参数索引  =  0
  交叉路径是否可用  =  否
           VPN名称  =  abc
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-RCAPLNK.md`
