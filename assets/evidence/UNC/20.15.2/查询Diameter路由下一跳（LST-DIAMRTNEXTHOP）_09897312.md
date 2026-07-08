# 查询Diameter路由下一跳（LST DIAMRTNEXTHOP）

- [命令功能](#ZH-CN_CONCEPT_0209897312__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897312__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897312__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897312__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897312__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0209897312__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897312)

**适用NF：PGW-C、SMF**

该命令用于查看已配置的Diameter路由下一跳信息。

#### [注意事项](#ZH-CN_CONCEPT_0209897312)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897312)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897312)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| REALMNAME | Diameter域名名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter路由的realm名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，必须是可见ASCII码，由软参BIT 150控制是否区分大小写。<br>默认值：无<br>配置原则：无 |
| APPLICATION | Diameter应用 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter路由的Diameter应用。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- GY：Gy接口应用。<br>- GX：Gx接口应用。<br>- S6B：S6b接口应用。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209897312)

- 显示指定realm名的Diameter路由下一跳信息，realm名为“example.com”：
  ```
  LST DIAMRTNEXTHOP:REALMNAME="example.com";
  ```
  ```

  RETCODE = 0  操作成功。

  Diameter路由下一跳信息
  ----------------
  Diameter域名名称             Diameter应用    下一跳               序号

  example.com                  Gx              host1                1  
  example.com                  Gx              host2                2
    (结果个数 = 2)
  ---    END
  ```
- 显示所有Diameter路由下一跳信息：
  ```
  LST DIAMRTNEXTHOP:;
  ```
  ```

  RETCODE = 0  操作成功。

  Diameter路由下一跳信息
  ----------------
  Diameter域名名称             Diameter应用    下一跳               序号

  example.com                  Gx               host1               1
  example.com                  Gx               host2               2      
  example1.com                 Gy               host3               1     
  (结果个数 = 3)
  ---    END
  ```

#### [输出结果说明](#ZH-CN_CONCEPT_0209897312)

参见ADD DIAMRTNEXTHOP的参数说明。
