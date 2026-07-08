---
id: UDG@20.15.2@MMLCommand@DSP SFEFASTPINGPKTSTC
type: MMLCommand
name: DSP SFEFASTPINGPKTSTC（显示SFE Fast-ping报文统计信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SFEFASTPINGPKTSTC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- Ping快回报文统计
status: active
---

# DSP SFEFASTPINGPKTSTC（显示SFE Fast-ping报文统计信息）

## 功能

该命令用于显示SFE fast-ping报文统计信息。

## 注意事项

- 只有在打开了ping快回使能开关后，才会对ping快回报文进行统计计数。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。区分大小写。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |

## 操作的配置对象

- [SFE Fast-ping报文统计信息（SFEFASTPINGPKTSTC）](configobject/UDG/20.15.2/SFEFASTPINGPKTSTC.md)

## 使用实例

- 显示指定RU的fast-ping报文统计信息：
  ```
  DSP SFEFASTPINGPKTSTC:RUNAME="VNODE_VNRS_VNFC_IPU_0064";
  ```
  ```

  RETCODE = 0  操作成功。                                                 
                                                                                
  结果如下                                                       
  -------------------------                                                       
  RU名称                      报文类型         报文数量
  VNODE_VNRS_VNFC_IPU_0064    IPv4 ping快回请求     15                          
  VNODE_VNRS_VNFC_IPU_0064    IPv4 ping快回应答     15   
  VNODE_VNRS_VNFC_IPU_0064    IPv6 ping快回请求    15                          
  VNODE_VNRS_VNFC_IPU_0064    IPv6 ping快回应答    15                         
  (结果个数 = 4)                                                         
  ---    END
  ```
- 显示所有RU的fast-ping报文统计信息：
  ```
  DSP SFEFASTPINGPKTSTC:;
  ```
  ```

  RETCODE = 0  操作成功。                                          
                                                                                
  结果如下                                                       
  -------------------------                                                       
  RU名称                      报文类型         报文数量
  VNODE_VNRS_VNFC_IPU_0064    IPv4 ping快回请求     15                          
  VNODE_VNRS_VNFC_IPU_0064    IPv4 ping快回应答     15   
  VNODE_VNRS_VNFC_IPU_0064    IPv6 ping快回请求     15                          
  VNODE_VNRS_VNFC_IPU_0064    IPv6 ping快回应答     15                           
  VNODE_VNRS_VNFC_IPU_0065    IPv4 ping快回请求     0                           
  VNODE_VNRS_VNFC_IPU_0065    IPv4 ping快回应答     0   
  VNODE_VNRS_VNFC_IPU_0065    IPv6 ping快回请求     15                          
  VNODE_VNRS_VNFC_IPU_0065    IPv6 ping快回应答     15                            
  (结果个数 = 8)                                                         
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示SFE-Fast-ping报文统计信息（DSP-SFEFASTPINGPKTSTC）_00440865.md`
