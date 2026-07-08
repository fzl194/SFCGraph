---
id: UDG@20.15.2@MMLCommand@LST LOGICINF
type: MMLCommand
name: LST LOGICINF（查询逻辑接口）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: LOGICINF
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- DN管理
- 逻辑接口管理
- 逻辑接口配置
- 接口
status: active
---

# LST LOGICINF（查询逻辑接口）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于显示逻辑接口的相关信息。

## 注意事项

默认为输出所有逻辑接口配置信息；若想查看指定逻辑接口配置信息，可指定逻辑接口名称，如果输入的逻辑接口名称在系统中不存在，则查询失败。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NAME | 逻辑接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于配置逻辑接口名称，确保逻辑接口的唯一性。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：<br>- 字符串形式，用户输入形式例如：n4if1/0/0。其中n4if为逻辑接口类型；1/0/0中第一个数字为ISU组号，第二个数字为实例类型；第三个数字为逻辑接口号，各逻辑接口类型有各自的配置范围。<br>- 逻辑接口类型：giif，s5-sif，s1-uif，saif，paif，grpif，phif，s11-uif，nxccif，nxucif，n4if，n3if，n9cif，scif，vxlanif，n19if，tm3if，tx-uif，n6mbif，n3mbif，gcfif，swuif，swmif。（其中nxccif为预置接口，配置后只允许执行ping操作。）。<br>- ISU组号：1。<br>- ISU实例类型：0~64。0表示组级类型，1~64表示Instance级类型。<br>- ISU实例类型为0时，逻辑接口号：giif：0~1023，grpif：0，phif：0~2047，nxccif：0，n4if：0，tm3if：0，gcfif：0，swuif：0，swmif：0~15。<br>- ISU实例类型为1时，逻辑接口号：s5-sif：0~31，s1-uif：0~31，saif：0~31，paif：0~31，s11-uif：0~31，nxucif：0~31，n3if：0~31，n9cif：0~31，scif：0~31，vxlanif：0~31，n19if：0~31，tx-uif：0，n6mbif：0，n3mbif：0~31。<br>- ISU实例类型为2~64时，逻辑接口号: s5-sif：0，s1-uif：0，saif：0，paif：0，n3if：0，n9cif：0，scif：0。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@LOGICINF]] · 逻辑接口（LOGICINF）

## 使用实例

- 显示n4if1/0/0逻辑接口信息：
  ```
  LST LOGICINF: NAME="n4if1/0/0";
  ```
  ```

  RETCODE = 0  操作成功。

  逻辑接口信息
  ------------
             逻辑接口名称  =  n4if1/0/0
      逻辑接口的IPv4地址1  =  192.168.123.166
      逻辑接口的IPv4掩码1  =  255.255.255.255
      逻辑接口的IPv4地址2  =  NULL
      逻辑接口的IPv4掩码2  =  NULL
  IPv4逻辑接口MTU（字节）  =  1500
              VPN实例名称  =  _public_
         逻辑接口的IP版本  =  IPv4
      逻辑接口的IPv6地址1  =  ::
  IPv6逻辑接口MTU（字节）  =  0
            IPv6前缀长度1  =  0
             接口切片属性  =  不使能
  (结果个数 = 1)
  ---    END
  ```
- 显示所有的逻辑接口信息：
  ```
  LST LOGICINF:;
  ```
  ```

  RETCODE = 0  操作成功。

  逻辑接口信息
  ------------
  逻辑接口名称  逻辑接口的IPv4地址1  逻辑接口的IPv4掩码1  逻辑接口的IPv4地址2  逻辑接口的IPv4掩码2  IPv4逻辑接口MTU（字节）  VPN实例名称  逻辑接口的IP版本  逻辑接口的IPv6地址1  IPv6逻辑接口MTU（字节）  IPv6前缀长度1  接口切片属性  

  n3if1/1/0     192.168.123.166      255.255.255.255      NULL                 NULL                 1500                     _public_     IPv4              ::                   0                        0              不使能        
  n4if1/0/0     192.168.128.168      255.255.255.255      NULL                 NULL                 1500                     _public_     IPv4              ::                   0                        0              不使能       
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-LOGICINF.md`
