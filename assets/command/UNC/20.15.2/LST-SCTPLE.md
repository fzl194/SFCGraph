---
id: UNC@20.15.2@MMLCommand@LST SCTPLE
type: MMLCommand
name: LST SCTPLE（查询SCTP本地实体）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SCTPLE
command_category: 查询类
applicable_nf:
- MME
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- SCTP本地实体
status: active
---

# LST SCTPLE（查询SCTP本地实体）

## 功能

**适用网元：MME、AMF**

该命令用于查看SCTP链路本地实体配置数据。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCTPLEIDX | SCTP本端实体索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SCTP本端实体索引用于唯一标识一个SCTP本端实体。<br>取值范围：整数类型，取值范围为0~1023。<br>默认值：无 |
| SCTPGROUPID | SCTP本端实体组标识 | 参数含义：该参数用于指定SCTP本端实体所属的组多个SCTP本端实体可以添加到一个实体组中，供NGAP（NG Application Protocol）和SFGAP（SFG Application Protocol）协议层使用该参数通过<br>[**ADD SCTPLEGRP**](../SCTP本地实体组/增加SCTP本地实体组(ADD SCTPLEGRP)_19186931.md)<br>命令配置。<br>取值范围：整数类型，取值范围为0~255。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCTPLE]] · SCTP本地实体（SCTPLE）

## 使用实例

1. 输入SCTP链路本地实体索引和所属SCTP本地实体组索引，查询指定的SCTP链路数据：
  ```
  %%LST SCTPLE: SCTPLEIDX=1, SCTPGROUPID=1;%% 
  ```
  ```
  RETCODE = 0  操作成功  

  The result is as follows 
  ------------------------       
               SCTP本端实体索引  =  1 
             SCTP本端实体组索引  =  1          
                  本地IPv4地址1  =  10.100.0.0          
                  本地IPv4地址2  =  0.0.0.0                      
                         端口号  =  36412                 
               交叉路径是否可用  =  not support cross          
               SCTP协议参数索引  =  0                     
                           用途  =  use range both UE and NONUE                        
                           权重  =  100                   
                           描述  =  NULL (Number of results = 1)  

  ---    END 
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SCTPLE.md`
