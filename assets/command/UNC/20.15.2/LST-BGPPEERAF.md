---
id: UNC@20.15.2@MMLCommand@LST BGPPEERAF
type: MMLCommand
name: LST BGPPEERAF（查询BGP对等体地址族）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: BGPPEERAF
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- BGP对等体地址族
status: active
---

# LST BGPPEERAF（查询BGP对等体地址族）

## 功能

该命令用于查询相应BGP IPv4或IPv6对等体地址族配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| AFTYPE | 地址族类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv4vpn：VPNv4地址族。<br>- ipv6uni：IPv6地址族。<br>- ipv6vpn：VPNv6地址族。<br>默认值：无 |
| ADDRESSTYPE | 地址类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv6uni”时为可选参数。<br>参数含义：该参数用于指定对等体的地址类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4：IPv4。<br>- ipv6：IPv6。<br>默认值：无 |
| REMOTEADDRESS | IPv4对等体地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni”、“ipv4vpn” 或 “ipv6vpn”时为可选参数。<br>可选必选说明：条件可选参数<br>前提条件：该参数在“ADDRESSTYPE”配置为“ipv4”时为可选参数。<br>参数含义：该参数用于指定连接对等体的IPv4接口地址。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。<br>默认值：无 |
| REMOTEADDRESSV6 | IPv6对等体地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ADDRESSTYPE”配置为“ipv6”时为可选参数。<br>参数含义：该参数用于指定连接对等体的IPv6接口地址。<br>数据来源：对端协商<br>取值范围：IPv6地址类型。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/BGPPEERAF]] · BGP对等体地址族（BGPPEERAF）

## 使用实例

- 查询相应BGP IPv4对等体地址族配置：
  ```
  LST BGPPEERAF:VRFNAME="_public_",AFTYPE=ipv4uni;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
                   VPN实例名称  =  _public_
                    地址族类型  =  IPv4uni
                      地址类型  =  IPv4
                IPv4对等体地址  =  10.2.2.2
                IPv6对等体地址  =  ::
              所属对等体组名称  =  NULL
                  团体属性发布  =  FALSE
              扩展团体属性发布  =  FALSE
              扩展团体属性丢弃  =  FALSE
                  允许AS号重复  =  FALSE
                允许AS号重复数  =  NULL
              允许缺省路由通告  =  FALSE
              缺省路由通告策略  =  NULL
        带条件匹配缺省路由发布  =  NULL
              全局路由更新保存  =  FALSE
                下一跳处理模式  =  NULL
                    路由首选值  =  0
                仅携带公有AS号  =  FALSE
                  路由超限阈值  =  NULL
                路由超限百分比  =  75
              路由超限告警类型  =  缺省值
             超时定时器（min）  =  NULL
             路由更新时间（s）  =  15
                路由反射器客户  =  FALSE
               替换AS Path属性  =  FALSE
                  引入路由策略  =  NULL
                  发布路由策略  =  NULL
              引入前缀过滤策略  =  NULL
              发布前缀过滤策略  =  NULL
           接收路由AS Path过滤  =  NULL
           发布路由AS Path过滤  =  NULL
           接收路由ACL规则标识  =  NULL
           发布路由ACL规则标识  =  NULL
      是否发布bestExternal路由  =  FALSE
  向邻居发布多少条add-path路由  =  NULL
                  add-path模式  =  空
              强制删除私有AS号  =  FALSE
            删除左边的私有AS号  =  FALSE
  用本地AS号替换所有的私有AS号  =  FALSE
           不忽略BGP邻居的AS号  =  FALSE
          接收路由ACL6规则标识  =  NULL
          发布路由ACL6规则标识  =  NULL
          引入IPv6前缀过滤策略  =  NULL
          发布IPv6前缀过滤策略  =  NULL
            迭代多源邻居源接口  =  FALSE
  (结果个数 = 1)
  ---    END
  ```
- 查询相应BGP IPv6对等体地址族配置：
  ```
  LST BGPPEERAF:VRFNAME="_public_",AFTYPE=ipv6uni;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
                   VPN实例名称  =  _public_
                    地址族类型  =  IPv6uni
                      地址类型  =  IPv6
                IPv4对等体地址  =  0.0.0.0
                IPv6对等体地址  =  2001:db8:1:1:1:1:1:1
              所属对等体组名称  =  NULL
                  团体属性发布  =  FALSE
              扩展团体属性发布  =  FALSE
              扩展团体属性丢弃  =  FALSE
                  允许AS号重复  =  FALSE
                允许AS号重复数  =  NULL
              允许缺省路由通告  =  FALSE
              缺省路由通告策略  =  NULL
        带条件匹配缺省路由发布  =  NULL
              全局路由更新保存  =  FALSE
                下一跳处理模式  =  NULL
                    路由首选值  =  0
                仅携带公有AS号  =  FALSE
                  路由超限阈值  =  NULL
                路由超限百分比  =  75
              路由超限告警类型  =  缺省值
             超时定时器（min）  =  NULL
             路由更新时间（s）  =  15
                路由反射器客户  =  FALSE
               替换AS Path属性  =  FALSE
                  引入路由策略  =  NULL
                  发布路由策略  =  NULL
              引入前缀过滤策略  =  NULL
              发布前缀过滤策略  =  NULL
           接收路由AS Path过滤  =  NULL
           发布路由AS Path过滤  =  NULL
           接收路由ACL规则标识  =  NULL
           发布路由ACL规则标识  =  NULL
      是否发布bestExternal路由  =  FALSE
  向邻居发布多少条add-path路由  =  NULL
                  add-path模式  =  空
              强制删除私有AS号  =  FALSE
            删除左边的私有AS号  =  FALSE
  用本地AS号替换所有的私有AS号  =  FALSE
           不忽略BGP邻居的AS号  =  FALSE
          接收路由ACL6规则标识  =  NULL
          发布路由ACL6规则标识  =  NULL
          引入IPv6前缀过滤策略  =  NULL
          发布IPv6前缀过滤策略  =  NULL
            迭代多源邻居源接口  =  FALSE
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询BGP对等体地址族（LST-BGPPEERAF）_00840717.md`
