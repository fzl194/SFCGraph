---
id: UNC@20.15.2@MMLCommand@LST INTERFACEIPSEC
type: MMLCommand
name: LST INTERFACEIPSEC（查询接口）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: INTERFACEIPSEC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- 接口管理
- 接口配置
status: active
---

# LST INTERFACEIPSEC（查询接口）

## 功能

该命令用于查询设备上接口的信息。设备接口包括逻辑接口及物理接口。物理接口是真实存在的接口。逻辑接口是指能够实现数据交换功能但物理上不存在、需要通过配置建立的接口。

## 注意事项

该命令在VNFP和VNFC上都可以执行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [接口（INTERFACEIPSEC）](configobject/UNC/20.15.2/INTERFACEIPSEC.md)

## 使用实例

- 不指定IFNAME参数时，查询所有接口的信息：
  ```
  LST INTERFACEIPSEC:;
  RETCODE = 0  操作成功

  结果如下
  -------------------------
  接口名                  接口类别     接口类型     接口编号    接口描述     管理状态    接口最大传输单元 (byte)    接口MAC地址       VPN实例名称         接口不分片标记    接口统计使能标记    接口Trap使能标记   主接口名    Trunk接口名    接口统计时间间隔 (s) 
  NULL0                   主接口       Null接口         0           NULL         接口up      1500                        0000-0000-0000    _public_            FALSE             使能                TRUE               NULL        NULL           300
  GigabitEthernet0/0/1    主接口       内联管理接口 0/0/1       NULL         接口up      1500                        1412-2311-3600    __mpp_vpn_inner__   FALSE             使能                TRUE               NULL        NULL           300
  LoopBack4               主接口       Loopback接口 4           a            接口up      1500                        0000-0000-0000    _public_            FALSE             使能                TRUE               NULL        NULL           300
  (结果个数 = 3)
  ---   END
  ```
- 查询指定接口的信息，接口名为LoopBack4：
  ```
  LST INTERFACEIPSEC: IFNAME="LoopBack4";
  RETCODE = 0  操作成功

  结果如下
  -------------------------
                 接口名  =  LoopBack4
       是否是子接口  =  FALSE
              接口类型  =  Null
              接口编号  =  NULL
              接口描述  =  huawei
              管理状态  =  Down
  接口最大传输单元 (byte)  =  0
      接口MAC地址  =  NULL
      VPN实例名称  =  NULL
   接口不分片标记  =  FALSE
  接口统计使能标记  =  FALSE 
  接口Trap使能标记  =  FALSE
             主接口名  =  NULL
        Trunk接口名  =  NULL
  接口统计时间间隔 (s)  =  0
  (结果个数 = 1) 
  ---   END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询接口（LST-INTERFACEIPSEC）_80592504.md`
