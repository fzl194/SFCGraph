---
id: UNC@20.15.2@MMLCommand@LST NRFFUNCSW
type: MMLCommand
name: LST NRFFUNCSW（查询NRF功能开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFFUNCSW
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF功能开关
status: active
---

# LST NRFFUNCSW（查询NRF功能开关）

## 功能

**适用NF：NRF**

该命令用于查询NRF的功能开关。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [NRF功能开关（NRFFUNCSW）](configobject/UNC/20.15.2/NRFFUNCSW.md)

## 使用实例

查询NRF功能开关：

```
LST NRFFUNCSW:;
%%LST NRFFUNCSW:;%%
RETCODE = 0  执行成功

结果如下
--------
                              NF访问记录开关  =  打开
                            服务发现记录开关  =  打开
                            负载变更通知开关  =  打开
                      NF Profile参数精简开关  =  打开
            状态通知中NF Profile参数精简开关  =  关闭
                        服务发现结果过滤开关  =  打开
                                数据核查开关  =  打开
                                周期时长(分)  =  1000
                           AMF可用性增强开关  =  关闭
                                授权功能开关  =  关闭
                    服务发现结果精确匹配开关  =  关闭
               跨NRF服务发现结果精确匹配开关  =  打开
                    服务发现结果位置匹配开关  =  打开
                服务发现结果位置匹配增强开关  =  关闭
                        号段导入数据可用开关  =  关闭
                                内部统计开关  =  关闭
                    主备容灾业务消息转发开关  =  关闭
                    号段导入功能数据核查开关  =  关闭
                   Token分配携带PLMN控制开关  =  关闭
                             NRF增量通知开关  =  关闭
                    通知携带全量配置号段开关  =  关闭
                        分层转发环路告警开关  =  打开
                分层转发环境告警恢复时长(秒)  =  1200
                          管理类消息流控开关  =  打开
                          发现类消息流控开关  =  打开
                            号段最长匹配开关  =  关闭
                    号段导入功能密钥核查开关  =  关闭
                         DNN网络标识匹配开关  =  关闭
                                 Via功能开关  =  打开
      服务发现结果过滤UNDISCOVERABLE状态开关  =  打开
                        号段NF无号段屏蔽开关  =  打开
                    服务发现参数防呆机制开关  =  打开
                  NF心跳类型变更增量通知开关  =  关闭
                      数组类信元判重校验开关  =  打开
                    服务发现分层转发优化开关  =  打开
          订阅响应location字段IP类型选择开关  =  打开
                        服务发现跟踪裁剪开关  =  打开
                              NF链路探测开关  =  打开
                  NF链路探测故障观察时长(秒)  =  120
                             BSFINFO裁剪开关  =  打开
                          心跳不切换接入开关  =  打开
           NRF支持无主用AMF时重选备份AMF开关  =  打开
                    服务发现结果切片缓存开关  =  打开
                服务发现结果配置号段缓存开关  =  打开
                        链路探测协议优选开关  =  关闭
               MBSMF服务发现结果精确匹配开关  =  打开
                        链路探测使用FQDN开关  =  关闭
            IPDOMAIN最长后缀匹配转发路由开关  =  打开
                            发现关口局NF开关  =  关闭
           服务发现结果携带InterPlmnFqdn开关  =  关闭
                   通知携带InterPlmnFqdn开关  =  关闭
               服务发现I-SMF精确匹配优选开关  =  关闭
 NF服务发现结果为空且NRF上无路由时返回值开关  =  关闭
服务发现结果是否携带NoProfileMatchReason开关  =  关闭
 东西向NRF实例组分层路由配置错误告警上报开关  =  打开
   南向NRF实例组分层路由配置错误告警上报开关  =  打开
           NRF实例组路由冲突告警恢复时长(秒)  =  3600
(结果个数 = 1) 

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NRF功能开关（LST-NRFFUNCSW）_09652285.md`
