# 查询BGP对等体组地址族（LST BGPPEERGROUPAF）

- [命令功能](#ZH-CN_CONCEPT_0000001549802058__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001549802058__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001549802058__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001549802058__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001549802058__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000001549802058__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001549802058)

该命令用于查看BGP对等体组地址族的配置。

#### [注意事项](#ZH-CN_CONCEPT_0000001549802058)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001549802058)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001549802058)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| AFTYPE | 地址族类型 | 可选必选说明：可选参数<br>参数含义：该参数用于给定VRF的地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv4vpn：VPNv4地址族。<br>- ipv6uni：IPv6地址族。<br>- ipv6vpn：VPNv6地址族。<br>默认值：无 |
| GROUPNAME | 对等体组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定相应的对等体组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～47。<br>默认值：无<br>配置原则：使用LST BGPPEERGROUP命令查看可用对等体组名。 |

#### [使用实例](#ZH-CN_CONCEPT_0000001549802058)

- 查看BGP IPv4对等体组地址族的配置：
  ```
  LST BGPPEERGROUPAF:VRFNAME="_public_",GROUPNAME="asdf",AFTYPE=ipv4uni;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
                   VPN实例名称  =  _public_
                    地址族类型  =  IPv4uni
                  对等体组名称  =  asdf
                  对等体组类型  =  IBGP
                  团体属性发布  =  FALSE
              扩展团体属性发布  =  FALSE
              扩展团体属性丢弃  =  FALSE
                  允许AS号重复  =  FALSE
                允许AS号重复数  =  NULL
              允许缺省路由通告  =  FALSE
              缺省路由通告策略  =  NULL
        带条件匹配缺省路由发布  =  NULL
                  路由更新保存  =  FALSE
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
  (结果个数 = 1)
  ---    END
  ```
- 查看BGP IPv6对等体组地址族的配置：
  ```
  LST BGPPEERGROUPAF:VRFNAME="_public_",GROUPNAME="asdf",AFTYPE=ipv6uni;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
                   VPN实例名称  =  _public_
                    地址族类型  =  IPv6uni
                  对等体组名称  =  asdf
                  对等体组类型  =  IBGP
                  团体属性发布  =  FALSE
              扩展团体属性发布  =  FALSE
              扩展团体属性丢弃  =  FALSE
                  允许AS号重复  =  FALSE
                允许AS号重复数  =  NULL
              允许缺省路由通告  =  FALSE
              缺省路由通告策略  =  NULL
        带条件匹配缺省路由发布  =  NULL
                  路由更新保存  =  FALSE
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
  (结果个数 = 1)
  ---    END
  ```

#### [输出结果说明](#ZH-CN_CONCEPT_0000001549802058)

参见ADD BGPPEERGROUPAF的参数说明。
