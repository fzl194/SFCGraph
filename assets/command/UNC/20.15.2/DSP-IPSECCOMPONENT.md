---
id: UNC@20.15.2@MMLCommand@DSP IPSECCOMPONENT
type: MMLCommand
name: DSP IPSECCOMPONENT（查询IPsec组件信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: IPSECCOMPONENT
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
- IPsec组件信息
status: active
---

# DSP IPSECCOMPONENT（查询IPsec组件信息）

## 功能

该命令用于查询IPsec组件信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TYPE | 显示类型 | 可选必选说明：必选参数<br>参数含义：显示IPsec组件不同信息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- COMP_INFO：显示IPsec组件信息。<br>- SOCK_INFO：显示Ipsec组件创建的SOCKET信息。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IPSECCOMPONENT]] · IPsec组件信息（IPSECCOMPONENT）

## 使用实例

- 查询IPsec组件信息：
  ```
  DSP IPSECCOMPONENT: TYPE=COMP_INFO;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
  IPsec组件PID    IPsec组件CID    部署类型    OS节点ID     端口组ID1    端口组ID2    PP6组件PID    PP6组件状态    PP6写管道ID    PP6读管道ID    PP6写管道状态    PP6管道打开重传定时器状态    PP6流控定时器状态    PP4组件PID    PP4组件状态    PP4写管道ID    PP4读管道ID    PP4写管道状态    PP4管道打开重传定时器状态    PP4流控定时器状态    Socket组件CID    Socket组件状态    Socket注册状态    Socket注册定时器状态    Socket NSF BB状态    Socket NSF BB定时器状态    应用切换状态    应用切换定时器状态

  0x3f0050        0x803f0098      1           1            0            0            0x72000f      可用状态       524442         0              已打开状态       未运行状态                   未运行状态           0x660014      可用状态       524443         0              已打开状态       未运行状态                   未运行状态           0x8065000b       可用状态          已注册状态        未运行状态              4                    未运行状态                 初始状态        未运行状态        
  0x3f0022        0x803f0022      2           134217794    65           66           0x72000f      可用状态       2148008018     0              已打开状态       未运行状态                   未运行状态           0x660014      可用状态       0              0              初始状态         未运行状态                   未运行状态           0x80650094       可用状态          已注册状态        未运行状态              初始状态             未运行状态                 初始状态        未运行状态        
  0x3f0021        0x803f0021      2           134217793    65           66           0x72000f      可用状态       2148008014     0              已打开状态       未运行状态                   未运行状态           0x660014      可用状态       0              0              初始状态         未运行状态                   未运行状态           0x80650087       可用状态          已注册状态        未运行状态              初始状态             未运行状态                 初始状态        未运行状态        
  (结果个数 = 3)
  ---    END
  ```
- 查询IPsec socket信息：
  ```
  DSP IPSECCOMPONENT: TYPE=SOCK_INFO;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
  IPsec组件PID    IPsec组件CID    ESP socket ID    ESP socket FSM状态    ESP发送管道ID    ESP发送管道状态    ESP管道打开重传定时器状态    ESP流控定时器状态    AH socket ID    AH socket FSM状态    AH发送管道ID    AH发送管道状态    AH管道打开重传定时器状态    AH流控定时器

  0x3f0050        0x803f0098      9                已创建状态            524453           已打开状态         未运行状态                   未运行状态           10              已创建状态           524455          已打开状态        未运行状态                  未运行状态  
  0x3f0022        0x803f0022      1                已创建状态            1572914          已打开状态         未运行状态                   未运行状态           2               已创建状态           524343          已打开状态        未运行状态                  未运行状态  
  0x3f0021        0x803f0021      1                已创建状态            2097204          已打开状态         未运行状态                   未运行状态           2               已创建状态           1572918         已打开状态        未运行状态                  未运行状态  
  (结果个数 = 3)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-IPSECCOMPONENT.md`
